from celery import shared_task
from django.contrib.auth.models import User
from django.conf import settings

from analytics.dota.algo_dota import DotaAnalysing
from analytics.cs_go.algo_cs_go import CSGOAnalysing
from analytics.overwatch.algo_overwatch import Overwatch


@shared_task
def dota_count(user_id: int):
    user = User.objects.get(pk=user_id)
    steam_id = user.talantuser.steam_id

    dota = DotaAnalysing(steam_id, user.talantuser.dota_result)
    try:
        dota.start()
    except Exception as e:
        raise e
    finally:
        user.talantuser.dota_task = None
        user.talantuser.save()


@shared_task
def cs_count(user_id: int):
    user = User.objects.get(pk=user_id)
    steam_id = user.talantuser.steam_id

    cs = CSGOAnalysing(settings.STEAM_API_KEY, steam_id, user.talantuser.cs_result)
    try:
        cs.start()
    except Exception as e:
        raise e
    finally:
        user.talantuser.cs_task = None
        user.talantuser.save()


@shared_task
def overwatch_count(user_id: int):
    user = User.objects.get(pk=user_id)
    battle_tag = user.talantuser.blizzard_battletag

    overwatch = Overwatch(battle_tag, user.talantuser.overwatch_result)
    try:
        pass
        # overwatch.start()
    except Exception as e:
        raise e
    finally:
        user.talantuser.overwatch_task = None
        user.talantuser.save()
