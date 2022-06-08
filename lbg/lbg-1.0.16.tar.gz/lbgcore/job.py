class Job:
    def __init__(self, client):
        self.client = client

    def list_by_page(self, job_group_id, status=None, page=1, per_page=50):
        params = {
            'page': page,
            'per_page': per_page
        }
        if status:
            params['status'] = status
        data = self.client.get(f'/data/job_group/{job_group_id}/jobs', params=params)
        return data

    def list_by_number(self, job_group_id, number, status=None):
        if status is None:
            status = []
        per_page = 50
        job_list = []
        data = self.list_by_page(job_group_id, page=1, per_page=per_page, status=status)
        total = data['total']
        per_page = data['per_page']
        page_number = 0
        while page_number * per_page < total:
            page_number = page_number + 1
            if page_number > 1:
                data = self.list_by_page(job_group_id, page=page_number, per_page=per_page, status=status)
            for each in data['items']:
                job_list.append(each)
                if number != -1 and len(job_list) >= number:
                    return job_list
        return job_list

    def delete(self, job_id):
        data = self.client.post(f"/data/job/{job_id}/del")
        return data

    def terminate(self, job_id):
        data = self.client.post(f"/data/job/{job_id}/terminate")
        return data

    def resubmit(self, job_id):
        data = self.client.post(f"/data/job/{job_id}/resubmit")
        return data

    def kill(self, job_id):
        data = self.client.post(f"/data/job/{job_id}/kill")
        return data

    def log(self, job_id):
        data = self.client.get(f"/data/job/{job_id}/log")
        return data

    def get_sts(self):
        data = self.client.get("/data/get_sts_token")
        return data

    def insert(self, **kwargs):
        must_fill = ['job_type', 'oss_path', 'program_id', 'scass_type', 'command', 'platform', 'image_name']
        for each in must_fill:
            if each not in kwargs:
                raise ValueError(f'{each} is required when submitting job')
        data = self.client.post("/data/v2/insert_job", data=kwargs)
        return data

    def detail(self, job_id):
        data = self.client.get(f"/data/job/{job_id}")
        return data

    def view_ls(self, job_id, path):
        if path == '':
            path = '/'
        params = {
            "path": path
        }
        data = self.client.post(f"/data/job/{job_id}/jcc/ls", data=params)
        return data.get('data', {})

    def view_read(self, job_id, path, start_byte=0, buf_size=8192):
        if path == '':
            path = '/'
        body = {
            "path": path
        }
        params = {
            'start_bytes': start_byte,
            'buf_size': buf_size
        }
        data = self.client.post(f"/data/job/{job_id}/jcc/read", data=body, params=params)
        return data.get('data', {})

    def view_state(self, job_id, path):
        if path == '':
            path = '/'
        params = {
            "path": path,
        }
        try:
            data = self.client.post(f"/data/job/{job_id}/jcc/state", data=params)
        except Exception as e:
            if 'no such file or directory' in str(e):
                return {}
            else:
                raise e
        return data.get('data', {})
