from rest_framework.routers import SimpleRouter

from .views import TodoViewset


router = SimpleRouter(trailing_slash=True)

router.register("todos", TodoViewset, basename="todos")

urlpatterns = router.urls
