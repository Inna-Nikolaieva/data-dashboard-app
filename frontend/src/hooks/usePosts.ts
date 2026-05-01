import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { PostsApi } from '../api/postsApi';
import type { Post, PostSort, UpdatePostPayload } from '../types/post';
import { useMemo } from 'react';

export const usePosts = (sort: PostSort = 'title') => {
  const queryClient = useQueryClient();

  const postsQuery = useQuery<Post[]>({
    queryKey: ['posts'],
    queryFn: PostsApi.getAllPosts,
  });

  const updatePost = useMutation<Post, Error, UpdatePostPayload>({
    mutationFn: ({ id, data }: UpdatePostPayload) =>
      PostsApi.updatePost(id, data),

    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });

  const deletePost = useMutation<void, Error, number>({
    mutationFn: (id: number) => PostsApi.deletePost(id),

    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });

  const posts = postsQuery.data ?? [];

  const sortedPosts = useMemo(() => {
    if (sort === 'none') return posts;

    return [...posts].sort((a, b) => {
      switch (sort) {
        case 'title':
          return a.title.localeCompare(b.title);

        case 'comments':
          return (b.comments?.length ?? 0) - (a.comments?.length ?? 0);

        default:
          return 0;
      }
    });
  }, [posts, sort]);

  return {
    posts: sortedPosts,
    hasPosts: sortedPosts.length > 0,
    isLoading: postsQuery.isLoading,
    isError: postsQuery.isError,
    updatePost: updatePost.mutate,
    deletePost: deletePost.mutate,
  };
};
