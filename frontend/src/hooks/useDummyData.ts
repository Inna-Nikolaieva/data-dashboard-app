import { useMutation, useQueryClient } from '@tanstack/react-query';
import { DummyDataApi } from '../api/dummyDataApi';
import type { ImportDummyDataResponse } from '../types/dummyData.ts';

export const useDummyData = () => {
  const queryClient = useQueryClient();

  const importMutation = useMutation<ImportDummyDataResponse>({
    mutationFn: DummyDataApi.importDummyData,

    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
      queryClient.invalidateQueries({ queryKey: ['users'] });
      queryClient.invalidateQueries({ queryKey: ['comments'] });
    },
  });

  return {
    importDummyData: importMutation.mutate,
    isLoading: importMutation.isPending,
    isSuccess: importMutation.isSuccess,
    isError: importMutation.isError,
  };
};
