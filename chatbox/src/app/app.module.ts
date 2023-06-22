import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { TranslateModule } from '@ngx-translate/core';

import { StreamAutocompleteTextareaModule, StreamChatModule } from 'stream-chat-angular';
import { AppComponent } from './app.component';
import { ChannelPreviewComponent } from './channel-preview/channel-preview.component';
import { MessageComponent } from './message/message.component';
//Importing required modules and components:
@NgModule({
  declarations: [AppComponent, MessageComponent, ChannelPreviewComponent],
  imports: [BrowserModule, TranslateModule.forRoot(), StreamAutocompleteTextareaModule, StreamChatModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
//this module configuration defines the components used in the application, imports required modules, and sets up the necessary dependencies
