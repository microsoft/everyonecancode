<template>
  <div class="chat-container">

    <div class="chat-messages" ref="chatMessages">
      <div class="message" v-for="(message, index) in messages" :key="index" :class="{ 'user-message': message.sender === 'user', 'responder-message': message.sender === 'responder' }">
        {{ message.content }}
      </div>
    </div>
    <div class="message-box">
      <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type your message...">
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
      newMessage: ''
    };
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() === '') return;

      // Add user message to the chat
      this.messages.push({
        content: this.newMessage,
        sender: 'user'
      });


      // Scroll to bottom of chat messages
      this.$refs.chatMessages.scrollTop = this.$refs.chatMessages.scrollHeight;
      try {
        const response = await axios.post('http://localhost:8000/chat', {
          message: this.newMessage
        });
        console.log(response)
        this.messages.push({
          content: response.data,
          sender: 'responder'
        });
        this.$refs.chatMessages.scrollTop = this.$refs.chatMessages.scrollHeight;
      } catch (error) {
        console.error('Error sending message:', error);

      }
      this.newMessage = '';
    }
  }
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 400px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}

.message {
  margin-bottom: 10px;
}

.user-message {
  text-align: right;
}

.responder-message {
  text-align: left;
  color: rgb(10, 90, 10);
}

.message-box {
  display: flex;
  padding: 10px;
}

.message-box input[type="text"] {
  flex: 1;
  padding: 5px;
}

.message-box button {
  padding: 5px 10px;
}
</style>
