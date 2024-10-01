<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiAccount, mdiMail, mdiAsterisk, mdiFormTextboxPassword, mdiGithub } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import BaseDivider from '@/components/BaseDivider.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import FormFilePicker from '@/components/FormFilePicker.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import UserCard from '@/components/UserCard.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import { updatePassword, updateCurrentUser } from '@/services/userService'
import NotificationBar from '@/components/alejo_components/NotificationBar.vue';

const mainStore = useMainStore()
const modalMessage = ref('');
const isAlertVisible = ref(false);
const isAlertUserVisible = ref(false);
const colorAlert = ref('');
const isModalVisible = ref(false);

const profileForm = reactive({
  name: mainStore.userName,
  email: mainStore.userEmail
})

const passwordForm = reactive({
  password_current: '',
  password: '',
  password_confirmation: ''
})
// mainStore.setUser(profileForm)

const submitProfile = async () => {
  if (profileForm.name !== mainStore.userName || profileForm.email !== mainStore.userEmail) {
    try {
      const response = await updateCurrentUser(
        profileForm.name,
        profileForm.email
      );

      modalMessage.value = "Perfil actualizado con éxito";
      isAlertUserVisible.value = true;
      colorAlert.value = 'success';

      setTimeout(() => {
        isAlertUserVisible.value = false;
      }, 10000);

      // Update the main store with the new user data
      mainStore.setUser({
        name: profileForm.name,
        email: profileForm.email
      });

      console.log('Profile actualizado');
    } catch (error) {

      modalMessage.value = 'Error al actualizar el perfil';
      isAlertUserVisible.value = true;
      colorAlert.value = 'danger';

      setTimeout(() => {
        isAlertUserVisible.value = false;
      }, 10000);

    }
  } else {
    modalMessage.value = 'No hay cambios en el perfil';

    isAlertUserVisible.value = true;
    colorAlert.value = 'danger';
    
    setTimeout(() => {
      isAlertUserVisible.value = false;
    }, 10000);
  
  }
}

const submitPass = async () => {
  if (passwordForm.password === passwordForm.password_confirmation) {
    try {
      const response = await updatePassword(
        passwordForm.password_current,
        passwordForm.password
      );
      modalMessage.value = "Contraseña actualizada con éxito";
      isAlertVisible.value = true;
      colorAlert.value = 'success';

      setTimeout(() => {
        isAlertVisible.value = false;
      }, 10000);

    } catch (error) {
      modalMessage.value = 'Error al actualizar la contraseña';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';

      setTimeout(() => {
        isAlertVisible.value = false;
      }, 10000);
    }
  } else {
    modalMessage.value = 'Las contraseñas no coinciden';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';

    setTimeout(() => {
      isAlertVisible.value = false;
    }, 10000);
  }
}
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiAccount" title="Perfil" main>
        <BaseButton
          href="https://github.com/justboil/admin-one-vue-tailwind"
          target="_blank"
          :icon="mdiGithub"
          label="Star on GitHub"
          color="contrast"
          rounded-full
          small
        />
      </SectionTitleLineWithButton>

      <UserCard class="mb-6" />

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <CardBox is-form @submit.prevent="submitProfile">
          <FormField label="Avatar" help="Max 500kb">
            <FormFilePicker label="Cargar" />
          </FormField>

          <NotificationBar
            v-if="isAlertUserVisible"
            :color="colorAlert" 
            :description="modalMessage"
            :visible="isModalVisible"
          />

          <FormField label="Nombre:" help="Requiere. Tu nombre">
            <FormControl
              v-model="profileForm.name"
              :icon="mdiAccount"
              name="username"
              required
              autocomplete="username"
            />
          </FormField>
          <FormField label="Correo:" help="Requiere. Tu correo">
            <FormControl
              v-model="profileForm.email"
              :icon="mdiMail"
              type="email"
              name="email"
              required
              autocomplete="email"
            />
          </FormField>

          <template #footer>
            <BaseButtons>
              <BaseButton color="info" type="submit" label="Enviar" />
            </BaseButtons>
          </template>
        </CardBox>

        <CardBox is-form @submit.prevent="submitPass">
          <NotificationBar
            v-if="isAlertVisible"
            :color="colorAlert" 
            :description="modalMessage"
            :visible="isModalVisible"
          />
          <FormField label="Contraseña actual:" help="Requiere. Tu contraseña actual">
            <FormControl
              v-model="passwordForm.password_current"
              :icon="mdiAsterisk"
              name="password_current"
              type="password"
              required
              autocomplete="current-password"
            />
          </FormField>

          <BaseDivider />

          <FormField label="Nueva contraseña:" help="Requiere. Nueva contraseña">
            <FormControl
              v-model="passwordForm.password"
              :icon="mdiFormTextboxPassword"
              name="password"
              type="password"
              required
              autocomplete="new-password"
            />
          </FormField>

          <FormField label="Confimar contraseña:" help="Requiere. Nueva contraseña una vez más">
            <FormControl
              v-model="passwordForm.password_confirmation"
              :icon="mdiFormTextboxPassword"
              name="password_confirmation"
              type="password"
              required
              autocomplete="new-password"
            />
          </FormField>

          <template #footer>
            <BaseButtons>
              <BaseButton type="submit" color="info" label="Enviar" />
            </BaseButtons>
          </template>
        </CardBox>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>
