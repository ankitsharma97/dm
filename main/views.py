from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from rest_framework import status

class BankListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        
        df = pd.read_csv('bank_branches.csv')
        df = df.dropna()
        df = df.drop_duplicates()

        unique_banks = df['bank_name'].unique()

        return Response(unique_banks)


class BranchSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):

        df = pd.read_csv('bank_branches.csv')
        df = df.dropna()
        df = df.drop_duplicates()

        branch_name = request.query_params.get('branch_name', None)
        ifsc_code = request.query_params.get('ifsc', None)

        if branch_name:
            branch_data = df[df['branch'].str.contains(branch_name, case=False, na=False)]
        elif ifsc_code:
            branch_data = df[df['ifsc'].str.upper() == ifsc_code.upper()]
        else:
            return Response({"error": "Please provide a branch name or IFSC code to search."}, status=status.HTTP_400_BAD_REQUEST)

        if not branch_data.empty:
            branch_details = branch_data.to_dict('records')
            return Response(branch_details, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Branch not found."}, status=status.HTTP_404_NOT_FOUND)