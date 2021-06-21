from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TalantUser, DotaResult, CsResult, OverwatchResult


class CsResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsResult
        fields = (
            'error', 'result',
            'result_num', 'result_str',
            'result_big_str', 'result_json',
        )


class DotaResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DotaResult
        fields = (
            'error', 'result',
            'result_num', 'result_str',
            'result_big_str', 'result_json',
        )


class OverwatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverwatchResult
        fields = (
            'error', 'result',
            'result_num', 'result_str',
            'result_big_str', 'result_json',
        )


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # 'username',
            'email',
            'id',
            'first_name',
            'last_name'
        )


class TalentUserSerializer(serializers.ModelSerializer):
    dota_result = DotaResultSerializer()
    cs_result = CsResultSerializer()
    overwatch_result = OverwatchResultSerializer()

    class Meta:
        model = TalantUser
        fields = (
            'pk', 'steam_id',
            'blizzard_id', 'blizzard_battletag',
            'dota_result', 'cs_result', 'overwatch_result',
            'dota_task', 'cs_task', 'overwatch_task',
        )
