import aiofiles
from message_objects.upload_output import UploadOutput
from utils.utils_id import UtilsId
from utils.utils_time import UtilsTime
from fastapi import APIRouter, Request


router_upload = APIRouter()
utils_id = UtilsId()
utils_time = UtilsTime()

@router_upload.post("/upload", response_model=UploadOutput)
async def upload(request: Request) -> UploadOutput:
    print(utils_time.format_timestamp_ms(utils_time.get_current_timestamp_ms()) + ': resource_upload.upload(): Started!')
    t1 = utils_time.get_current_timestamp_ms()

    # Determine extension
    content_type = str(request.headers.get('content-type'))
    if not content_type.startswith('video'):
        raise RuntimeError("We can't process anything except videos!")
    extension = content_type.replace('video/', '')

    id = utils_id.generate_uuid().replace('-', '')
    #folder = '/home/leo/tekleo/fileserver/output'
    folder = '/output'
    path = folder + '/' + id + '.' + extension
    print(utils_time.format_timestamp_ms(utils_time.get_current_timestamp_ms()) + ': resource_upload.upload(): Saving video to [' + path + ']')


    async with aiofiles.open(path, 'wb') as buffer:
        async for chunk in request.stream():
            # print('resource_upload.upload(): Saving chunk...')
            await buffer.write(chunk)

    t2 = utils_time.get_current_timestamp_ms()
    print(utils_time.format_timestamp_ms(utils_time.get_current_timestamp_ms()) + ': resource_upload.upload(): Took ' + str(t2-t1) + ' ms')
    print(utils_time.format_timestamp_ms(utils_time.get_current_timestamp_ms()) + ': resource_upload.upload(): Ended!')

    return UploadOutput(id, path, t1, t2)
