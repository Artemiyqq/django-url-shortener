from .models import Url


class Hashing:
    @classmethod
    def process_url(cls, url: str) -> str:
        if cls.is_this_a_new_url(url, False):
            hashed_url = '/' + str(hash(url))
            Url.objects.create(original=url,
                               shortened=f'{hashed_url}')
            return hashed_url
        else:
            return cls.get_hashed_url(url)

    @classmethod
    def get_hashed_url(cls, url: str) -> str:
        return Url.objects.get(original=url).shortened

    @classmethod
    def get_original_url(cls, url: str) -> str:
        return Url.objects.get(shortened=url).original

    @staticmethod
    def is_this_a_new_url(url: str, hashed: bool) -> bool:
        if hashed:
            return not Url.objects.filter(shortened=url).exists()
        return not Url.objects.filter(original=url).exists()
