//represents the TypeScript component file for the MessageComponent
import { Component, Input } from '@angular/core';
import { StreamMessage } from 'stream-chat-angular';

@Component({
  selector: 'app-message',
  template: `
    <div>
      <b>{{ message?.user?.name }}</b> {{ message?.text }}
    </div>
  `,
  styles: ['b {margin-right: 4px}'],
})
export class MessageComponent {
  @Input() message: StreamMessage | undefined;
  constructor() {}
}
//Overall, this component is responsible for rendering a message in the template. It receives a StreamMessage object as an input and displays the user's name and message text in a <div> element.
