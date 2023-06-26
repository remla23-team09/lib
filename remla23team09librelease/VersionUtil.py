import subprocess


class VersionUtil:
    @staticmethod
    def get_version():
        try:
            version_info = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()

            version_parts = version_info.split('-')

            if len(version_parts) > 1:
                tag, commits, commit_hash = version_parts[:3]
                version = tag[1:]
            else:
                version = version_info

        except subprocess.CalledProcessError:
            version = "Unknown"

        return version

