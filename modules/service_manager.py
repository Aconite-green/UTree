import yaml
import os

class ServiceManager:
    def __init__(self, folder_path):
        # 폴더 경로 설정
        self.folder_path = os.path.abspath(folder_path)
        self.yml_filename = 'user_info.yml'
        self.yml_path = os.path.join(self.folder_path, self.yml_filename)

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        
        # 파일이 없으면 YML 파일을 생성
        if not os.path.exists(self.yml_path):
            self.create_default_config()

    def create_default_config(self):
        """기본 YML 파일을 생성하는 함수"""
        default_data = {
            'user': {
                'used_before': False
            },
            'recent_files': {
                'project': None,
                'dll': None,
                'can': None
            }
        }
        with open(self.yml_path, 'w') as yml_file:
            yaml.dump(default_data, yml_file)
        print(f"YML 파일이 생성되었습니다: {self.yml_path}")

    def load_config(self):
        """YML 파일의 모든 정보를 가져오는 함수"""
        with open(self.yml_path, 'r') as yml_file:
            data = yaml.safe_load(yml_file)
        return data

    def _update_config(self, section, key, value):
        """YML 파일의 특정 정보를 수정하는 함수"""
        # 기존 데이터를 로드
        with open(self.yml_path, 'r') as yml_file:
            data = yaml.safe_load(yml_file)
        
        # 수정할 섹션과 키 확인 후 업데이트
        if section in data and key in data[section]:
            data[section][key] = value
        else:
            raise KeyError(f"{section} 또는 {key}가 YML 파일에 존재하지 않습니다.")
        
        # 수정된 내용을 다시 YML 파일에 저장
        with open(self.yml_path, 'w') as yml_file:
            yaml.dump(data, yml_file)

    def update_user_status(self, used_before):
        """사용자의 프로그램 사용 여부를 업데이트하는 함수"""
        self._update_config('user', 'used_before', used_before)

    def update_recent_project(self, project_name):
        """최근 사용한 프로젝트 파일 이름을 업데이트하는 함수"""
        self._update_config('recent_files', 'project', project_name)

    def update_recent_dll(self, dll_name):
        """최근 사용한 DLL 파일 이름을 업데이트하는 함수"""
        self._update_config('recent_files', 'dll', dll_name)

    def update_recent_can(self, can_name):
        """최근 사용한 CAN 파일 이름을 업데이트하는 함수"""
        self._update_config('recent_files', 'can', can_name)

    def get_user_status(self):
        """사용자의 프로그램 사용 여부를 반환하는 함수"""
        config_data = self.load_config()
        return config_data['user']['used_before']
    
    def get_recent_project(self):
        """최근 사용한 프로젝트 파일 이름을 반환하는 함수"""
        config_data = self.load_config()
        return config_data['recent_files']['project']
    
    def get_recent_dll(self):
        """최근 사용한 DLL 파일 이름을 반환하는 함수"""
        config_data = self.load_config()
        return config_data['recent_files']['dll']
    
    def get_recent_can(self):
        """최근 사용한 CAN 파일 이름을 반환하는 함수"""
        config_data = self.load_config()
        return config_data['recent_files']['can']