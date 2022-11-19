import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="PacMan.py", icon="assets/pacman2.ico"
)]


cx_Freeze.setup(
    name="PacMan",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]}},
    executables=arquivo
)