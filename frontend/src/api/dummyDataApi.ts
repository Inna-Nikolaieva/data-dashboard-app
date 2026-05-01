import apiClient from './client.ts';
import { DUMMY_DATA } from './routes.ts';
import type { ImportDummyDataResponse } from '../types/dummyData.ts';

export const DummyDataApi = {
  importDummyData: (): Promise<ImportDummyDataResponse> =>
    apiClient.post(DUMMY_DATA.importData()).then((res) => res.data),
};
