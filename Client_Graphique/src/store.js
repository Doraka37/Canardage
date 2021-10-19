import { createStore, combineReducers } from '@reduxjs/toolkit'
import UserInfos from './Store/Userinfos'

const rootReducer = combineReducers({
  UserInfos: UserInfos,
});

export default createStore(rootReducer);
