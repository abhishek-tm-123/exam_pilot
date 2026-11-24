from rest_framework import serializers

from assessment_management.models import Assessment

from datetime import datetime

class AssessmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assessment
        fields = "__all__"
        read_only_fields = ["id","slug","end_time","faculty","created_at","updated_at"]
        
    def validate(self,validated_data):
        exam_date = validated_data.get("exam_date")
        if exam_date < datetime.today().date():
            raise serializers.ValidationError("invalid date")
        
        
        return validated_data