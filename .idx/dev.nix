{ pkgs, ... }: {
  channel = "stable-24.11"; 
  
  # 여기에 사용할 도구들을 적습니다.
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.google-generativeai # 이 줄이 핵심!
    pkgs.python311Packages.requests
  ];

  idx = {
    extensions = [ "ms-python.python" ];
    workspace = {
      # 프로젝트가 처음 켜질 때 실행될 작업
      onCreate = {
        install-packages = "pip install google-generativeai requests";
      };
    };
  };
}