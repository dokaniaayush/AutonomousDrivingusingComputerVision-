'''
Builds and returns a simple CNN with 8 layers (6 conv, 2 fully connected).
Images are resized to INPUT_SIZExINPUT_SIZE.
'''
def createModel():
    model=Sequential()
    model.add(Conv2D(32, (3, 3), padding=’same’, activation=’relu’,input_shape=(INPUT_SIZE,INPUT_SIZE,3)))
    model.add(Conv2D(32, (3, 3), activation=’relu’))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding=’same’, activation=’relu’))
    model.add(Conv2D(64, (3, 3), activation=’relu’))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    
    model.add(Conv2D(64, (3, 3), padding=’same’, activation=’relu’))
    model.add(Conv2D(64, (3, 3), activation=’relu’))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512, activation=’relu’))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation=’softmax’))

    return model
