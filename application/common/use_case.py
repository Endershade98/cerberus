# application/common/use_case.py

from typing import Generic, TypeVar

from domain.shared.unit_of_work import UnitOfWork


Request = TypeVar("Request")
Response = TypeVar("Response")


class UseCase(Generic[Request, Response]):

    def __init__(self, uow: UnitOfWork):
        self.uow = uow


    def execute(
        self,
        request: Request,
    ) -> Response:

        with self.uow:

            result = self._execute(request)

            events = self._collect_events(result)

            if events:
                self.uow.collect(events)

            return result


    def _execute(
        self,
        request: Request,
    ) -> Response:
        raise NotImplementedError


    def _collect_events(
        self,
        result,
    ):

        if hasattr(result, "pull_events"):
            return result.pull_events()

        return []