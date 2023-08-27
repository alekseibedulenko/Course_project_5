from abc import abstractmethod, ABC


class BaseApi(ABC):
    def __init__(self, url, number_of_vacancies):
        self.url = url
        self.number_of_vacancies = number_of_vacancies

    @abstractmethod
    def _search_vacancies(self, employer_id):
        pass

    def get_vacancies(self, employer_id):
        pass


