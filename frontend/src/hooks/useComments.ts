import { useMutation, useQueryClient } from '@tanstack/react-query';
import { CommentsApi } from '../api/commentsApi';
import type { Comment, UpdateCommentPayload } from '../types/comment.ts';

export const useComments = () => {
  const queryClient = useQueryClient();

  const updateComment = useMutation<Comment, Error, UpdateCommentPayload>({
    mutationFn: ({ id, data }: UpdateCommentPayload) =>
      CommentsApi.updateComment(id, data),

    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['comments'] });
    },
  });

  const deleteComment = useMutation<void, Error, number>({
    mutationFn: (id: number) => CommentsApi.deleteComment(id),

    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['comments'] });
    },
  });

  return {
    updateComment: updateComment.mutate,
    deleteComment: deleteComment.mutate,
  };
};
